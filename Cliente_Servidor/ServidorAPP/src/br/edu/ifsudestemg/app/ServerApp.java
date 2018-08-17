package br.edu.ifsudestemg.app;

import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.ArrayList;
import java.util.Scanner;

import org.json.JSONArray;
import org.json.JSONObject;

import br.edu.ifsudestemg.modelo.Aluno;
import br.edu.ifsudestemg.modelo.Turma;

public class ServerApp {
	/**
	 * Inicia o servidor que irá aceitar as conexões com os clientes.  
	 */
	public static void main(String[] args) {
		try(ServerSocket server = new ServerSocket(23000)){
			
			while(true) {
				Socket cliente = server.accept();
				cliente.setSoTimeout(1000*30);
				String respostaJson = atenderCliente(cliente);
				exibirTurmasCadastradas(converterStringJson(respostaJson));
			}
				
		} catch (IOException e) {
			e.printStackTrace();
		}finally {
			System.out.println("Servidor será encerrado.");
		}
			
	}

	private static void exibirTurmasCadastradas(ArrayList<Turma> turmas) {
		for(Turma t : turmas) {
			String msg = String.format("A turma %s de %d do curso de %s possui %d alunos,"
					+ " dos quais %d estão matriculados.", t.getCurso(), t.getAno(), t.getCurso(),
					t.getAlunos().size(), t.getAlunos().size()-1);
			
			System.out.println(msg);
		}
	}

	private static ArrayList<Turma> converterStringJson(String stringJson) {
		JSONObject jsonObject = new JSONObject(stringJson);
		JSONArray jsonArrayTurmas = jsonObject.getJSONArray("turmas");
		
		ArrayList<Turma> turmas = new ArrayList<>();
		// Obtém cada turma do array turmas do objeto Json. 
		for(int i=0; i < jsonArrayTurmas.length(); i++) {
			JSONObject jsonObjectTurma = jsonArrayTurmas.getJSONObject(i);
			Turma turma = new Turma();
			turma.setId(jsonObjectTurma.getLong("id"));
			turma.setCurso(jsonObjectTurma.getString("curso"));
			turma.setAno(jsonObjectTurma.getInt("ano"));

			JSONArray jsonArrayAlunos = jsonObjectTurma.getJSONArray("alunos");
			// Obtém cada objeto aluno do objeto turma atual
			for(int j=0; j < jsonArrayAlunos.length(); j++) {
				JSONObject jsonObjectAluno = jsonArrayAlunos.getJSONObject(j);
				Aluno aluno = new Aluno();
				aluno.setId(jsonObjectAluno.getLong("id"));
				aluno.setNome(jsonObjectAluno.getString("nome"));
				aluno.setMatriculado(jsonObjectAluno.getBoolean("matriculado"));
				turma.getAlunos().add(aluno);
			}
			
			turmas.add(turma);
		}
		
		return turmas;
	}

	/**
	 * Recebe por parâmetro a conexão com o cliente. A partir dela lê todas as mensagens 
	 * enviadas pelo cliente até que seja enviado a mensagem 'exit', que indica 
	 * que a conexão pode ser encerrada. Retorna a mensagem enviada pelo cliente.
	 */
	private static String atenderCliente(Socket cliente) throws IOException{
		StringBuffer stringBuffer = new StringBuffer();
		
		try(Scanner inputStream = new Scanner(cliente.getInputStream())){
			
			String string = "";
			while(true) {
				if(!inputStream.hasNextLine())
					continue;
				
				string = inputStream.nextLine();
			
				if(string.equals("exit"))
					break;
				
				stringBuffer.append(string);
				string = "";
			}
			
		} catch (IOException e) { 
			e.printStackTrace();
		}
		
		System.out.println("Conexão com cliente será finalizada.");
		cliente.close();
		
		return stringBuffer.toString();
	}
}
