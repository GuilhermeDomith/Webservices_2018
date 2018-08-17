package br.edu.ifsudestemg.modelo;

public class Aluno {
	private long id;
	private String nome;
	private boolean matriculado;
	
	public Aluno() {
		nome = "";
	}

	public long getId() {
		return id;
	}

	public void setId(long id) {
		this.id = id;
	}

	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public boolean isMatriculado() {
		return matriculado;
	}

	public void setMatriculado(boolean matriculado) {
		this.matriculado = matriculado;
	}

	@Override
	public String toString() {
		return "Aluno [id=" + id + ", nome=" + nome + ", matriculado=" + matriculado + "]";
	}
	
}
