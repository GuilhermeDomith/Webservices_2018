package br.com.viacep;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.UnsupportedEncodingException;
import java.net.URL;
import java.net.URLConnection;

import javax.swing.JOptionPane;

public class ConsumirAPI {
	public static void main(String[] args) {

		while(true) {

			try {

				String cep = JOptionPane.showInputDialog("Fornça o cep:");
				if(cep == null) break;

				URLConnection con = obterConexaoViaCep(cep);
				BufferedReader input = getBufferedReader(con);

				String line;
				StringBuilder source = new StringBuilder();

				do {
					line = input.readLine();
					source.append(line);
				}while(line != null);

				input.close();
				
				JOptionPane.showMessageDialog(null, source.toString().replace(',', '\n'), 
						"Consulta CEP", JOptionPane.PLAIN_MESSAGE);
			}catch (Exception e) {
				System.out.println("Cep Inválido ou ocorreu uma falha na consulta");
				e.printStackTrace();
			}
		}
		
		System.exit(0);
	}

	private static URLConnection obterConexaoViaCep(String cep) throws IOException {
		URL url = new URL("https://viacep.com.br/ws/"+cep+"/json");
		return url.openConnection();

	}

	private static BufferedReader getBufferedReader(URLConnection con) throws UnsupportedEncodingException, IOException {
		return new BufferedReader(new InputStreamReader(con.getInputStream(), "utf-8"));
	}
}

