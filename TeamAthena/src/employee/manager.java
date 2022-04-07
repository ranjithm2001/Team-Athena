package employee;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JPanel;

import login.Index;

public class manager {
	public static JPanel manager_portal;
	public manager() {
		manager_portal = new JPanel();
		manager_portal.setLayout(null);
		
		JButton logout_button = new JButton("manager Logout");
		logout_button.setBounds(325, 320, 190, 25);
		logout_button.addActionListener(new ActionListener(){
			public void actionPerformed(ActionEvent e) {
				Index index = new Index();
				index.logout();
			}
		});
		manager_portal.add(logout_button);
	}
}
