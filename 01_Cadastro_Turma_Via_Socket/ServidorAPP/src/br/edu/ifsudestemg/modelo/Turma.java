package br.edu.ifsudestemg.modelo;

import java.util.ArrayList;

public class Turma {
	private long id;
	private String nome;
	private String curso;
	private int ano;
	private ArrayList<Aluno> alunos;
	
	public Turma() {
		curso = "";
		alunos = new ArrayList<>();
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

	public String getCurso() {
		return curso;
	}

	public void setCurso(String curso) {
		this.curso = curso;
	}

	public int getAno() {
		return ano;
	}

	public void setAno(int ano) {
		this.ano = ano;
	}

	public ArrayList<Aluno> getAlunos() {
		return alunos;
	}

	public void setAlunos(ArrayList<Aluno> alunos) {
		this.alunos = alunos;
	}

	@Override
	public String toString() {
		return "\nTurma [id=" + id + ", nome=" + nome + ", curso=" + curso + ", ano=" + ano + ", alunos=" + alunos + "]";
	}
	
}
