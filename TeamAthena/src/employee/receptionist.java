package employee;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JPanel;

import login.Index;

public class receptionist {
	public static JPanel receptionist_portal;
	public receptionist() {
		receptionist_portal = new JPanel();
		receptionist_portal.setLayout(null);
		
		JButton logout_button = new JButton("receptionist Logout");
		logout_button.setBounds(325, 320, 190, 25);
		logout_button.addActionListener(new ActionListener(){
			public void actionPerformed(ActionEvent e) {
				Index index = new Index();
				index.logout();
			}
		});
		receptionist_portal.add(logout_button);
	}
}
