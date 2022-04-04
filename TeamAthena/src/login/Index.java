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
import java.util.HashMap;
import java.util.Hashtable;
import java.util.Map;
import java.util.Properties;

import javax.imageio.ImageIO;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;

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

public class Index {
	protected JFrame frame;
	public JPanel Login_panel;
	public Connection connection = null;
	public VideoCapture capture;
	public Canvas canvas;
	public Boolean scanning=true;

	static{ System.loadLibrary(Core.NATIVE_LIBRARY_NAME); }
	
	public Index() {
		frame = new JFrame();
		frame.setSize(800, 500);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		Login_panel = new JPanel();
		frame.add(Login_panel);
		
		Login_panel.setLayout(null);
		
		canvas = new Canvas();
		canvas.setPreferredSize(new Dimension(400, 400));
		canvas.setBounds(10, 20, 400, 400);
		canvas.setBackground(Color.BLACK);
		Login_panel.add(canvas);
		frame.setVisible(true);
		
		scan_qr_code();
	}

	public static void main(String[] args) {
		new Index();
	}
	
	public void scan_qr_code() {
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
//							fetch_user_fromdb(scanned_details.get("username"), scanned_details.get("password"));
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
