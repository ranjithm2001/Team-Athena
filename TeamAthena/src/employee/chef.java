package employee;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JPanel;

import login.Index;

public class chef {
	public static JPanel kitchen_portal;
	public chef() {
		kitchen_portal = new JPanel();
		kitchen_portal.setLayout(null);
		
		JButton logout_button = new JButton("chef Logout");
		logout_button.setBounds(325, 320, 190, 25);
		logout_button.addActionListener(new ActionListener(){
			public void actionPerformed(ActionEvent e) {
				Index index = new Index();
				index.logout();
			}
		});
		kitchen_portal.add(logout_button);
	}
}
