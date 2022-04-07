package login;

import java.awt.Canvas;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.Image;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.image.BufferedImage;
import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.StringReader;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.HashMap;
import java.util.Hashtable;
import java.util.Map;
import java.util.Properties;

import javax.imageio.ImageIO;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;

import org.opencv.core.Core;
import org.opencv.core.Mat;
import org.opencv.core.MatOfByte;
import org.opencv.imgcodecs.Imgcodecs;
import org.opencv.videoio.VideoCapture;

import com.google.zxing.BinaryBitmap;
import com.google.zxing.DecodeHintType;
import com.google.zxing.LuminanceSource;
import com.google.zxing.MultiFormatReader;
import com.google.zxing.NotFoundException;
import com.google.zxing.Result;
import com.google.zxing.client.j2se.BufferedImageLuminanceSource;
import com.google.zxing.common.HybridBinarizer;

import employee.chef;
import employee.manager;
import employee.receptionist;

public class Index {
	protected static JFrame frame;
	public JPanel Login_panel;
	public Connection connection = null;
	public static VideoCapture capture;
	public static Canvas canvas;
	public static Boolean scanning=true;
	public static chef Kitchen_portal;
	public static manager manager_portal;
	public static receptionist recption_portal;
	public static Index login_page;


	static{ System.loadLibrary(Core.NATIVE_LIBRARY_NAME); }
	
	public Index() {
		
		Login_panel = new JPanel();
		Login_panel.setLayout(null);
		
		JLabel username_label = new JLabel("Username");
		username_label.setBounds(260, 120, 80, 25);
		Login_panel.add(username_label);
		JTextField usernameText = new JTextField(20);
		usernameText.setBounds(350, 120, 165, 25);
		Login_panel.add(usernameText);
			
		// password field
		JLabel pass_label = new JLabel("Password");
		pass_label.setBounds(260, 150, 80, 25);
		Login_panel.add(pass_label);
		JTextField pass_Text = new JTextField(20);
		pass_Text.setBounds(350, 150, 165, 25);
		Login_panel.add(pass_Text);
		
		JButton login_button = new JButton("Login");
		login_button.setBounds(325, 320, 190, 25);
		login_button.addActionListener(new ActionListener(){
			public void actionPerformed(ActionEvent e) {
				String username = usernameText.getText();
				String password = pass_Text.getText();
				String user_type = authorize_user(username, password);
				switch_panel(user_type);
			}
		});
		Login_panel.add(login_button);
		
		String jdbcUrl = "jdbc:sqlite:/run/media/gokul/f4b96ffb-3a6d-4ea0-865c-23f5f7cec76e/SE Project/Team-Athena/TeamAthena/users_data.db";
		try {
			connection = DriverManager.getConnection(jdbcUrl);
		} catch (SQLException e3) {
			System.out.println("Unable to connect to database");
		}
//		canvas = new Canvas();
//		canvas.setPreferredSize(new Dimension(400, 400));
//		canvas.setBounds(10, 20, 400, 400);
//		canvas.setBackground(Color.BLACK);
//		Login_panel.add(canvas);
		
//		scan_qr_code();
		
	}

	public static void main(String[] args) {
		login_page = new Index();
		
		frame = new JFrame();
		frame.setSize(800, 500);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setVisible(true);
		frame.add(login_page.Login_panel);

	}
	
	public void switch_panel(String user_type) {
		if(user_type.equals("Chef")) {
			Kitchen_portal = new chef();
			frame.remove(Login_panel);
			frame.add(Kitchen_portal.kitchen_portal);
			frame.revalidate();
		}
		else if(user_type.equals("Manager")) {
			manager_portal = new manager();
			frame.remove(Login_panel);
			frame.add(manager_portal.manager_portal);
			frame.revalidate();
		}
		else if(user_type.equals("Receptionist")) {
			recption_portal = new receptionist();
			frame.remove(Login_panel);
			frame.add(recption_portal.receptionist_portal);
			frame.revalidate();
		}
	}
	
	public void logout() {
		System.out.println("Logout successful");
		login_page = new Index();
		frame.getContentPane().removeAll();
		frame.repaint();
		frame.add(login_page.Login_panel);
		frame.revalidate();
	}
	
	public String authorize_user(String username, String password) {
//		String sql_command = "SELECT * FROM Employees WHERE Username='"+ username + "';";
//		Statement statement = null;
//		try {
//			statement = connection.createStatement();
//		} catch (SQLException e2) {
//			e2.printStackTrace();
//		}
//		try {
//			ResultSet result = statement.executeQuery(sql_command);
//			if (!result.getString("password").equals(password)) {
//				System.out.println("Wrong password");
//			}else {
//				if(result.getString("access_type").equals("Chef")) {
//					System.out.println("Chef has logged in");
//					return "Chef";
//				}
//				else if(result.getString("access_type").equals("Manager")) {
//					System.out.println("Manager has logged in");
//					return "Manager";
//				}
//				else if(result.getString("access_type").equals("Receptionist")) {
//					System.out.println("Receptionist has logged in");
//					return "Receptionist";
//				}
//			}
//		} catch (SQLException e2) {
//			System.out.println("Invalid username");
//		}
		return "";
	}

	
	public static void scan_qr_code() {
		capture = new VideoCapture(0);
		Mat cap_image = new Mat();
		Image img = null;
		if (capture.isOpened()) {
			while(scanning) {
				capture.read(cap_image);
				MatOfByte buffer = new MatOfByte();
				Imgcodecs.imencode(".png", cap_image, buffer);
				byte ba[] = buffer.toArray();
				Result scanned_stuff=null;
				try {
					img = ImageIO.read(new ByteArrayInputStream(ba));
					LuminanceSource source = new BufferedImageLuminanceSource((BufferedImage) img);
					BinaryBitmap bitmap = new BinaryBitmap(new HybridBinarizer(source));
					Hashtable<DecodeHintType, String> hints = new Hashtable<DecodeHintType, String>();
				      hints.put(DecodeHintType.CHARACTER_SET, "UTF-8");
					try {
						scanned_stuff = new MultiFormatReader().decode(bitmap, hints);
					} catch (NotFoundException e) {
					}
					if (scanned_stuff!=null) {
						String str = scanned_stuff.toString();
						
						Properties props = new Properties();
						props.load(new StringReader(str.substring(1, str.length() - 1).replace(", ", "\n")));       
						Map<String, String> scanned_details = new HashMap<String, String>();
						for (Map.Entry<Object, Object> e : props.entrySet()) {
							scanned_details.put((String)e.getKey(), (String)e.getValue());
						}
						if(scanned_details.get("Organization") == null) {
							System.out.println("Invalid QR code");
						}
						else if(scanned_details.get("Organization").equals("Salad_Corp")) {
//			fetch_user_fromdb(scanned_details.get("username"), scanned_details.get("password"));
							break;
						}
					}
				} catch (IOException e) {
					e.printStackTrace();
					capture.release();
					break;
				}
				canvas.getGraphics().drawImage(img, 0, 0, null);
			}
			if (!scanning) {
				capture.release();
			}
		}
	}

}
