// 1 - OBTENDO DATA COMPLETA ATUAL

const dataAtual = new Date();

// 2 - OBTENDO NOME DO DIA DA SEMANA ATUAL 

const diaAtual = new Date ();
const numeroDodiaatual = diaAtual.getDay();
    // ARRAY COM NOMES DOS DIAS DA SEMANA
    var arrayDiadasemana = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado'];
    // VINCULA NOME DO DIA NO ARRAY
    var nomeDodia = arrayDiadasemana[numeroDodiaatual];


// 3 - OBTENDO NOME DO MÊS ATUAL

const mesAtual = new Date ();
const numeroDomesatual = mesAtual.getMonth();
    // ARRAY COM NOMES DOS MESES
    var arrayMesesdoano = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho','Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'];
    // VINCULA NOME DO DIA NO ARRAY
    var nomeDomes = arrayMesesdoano[numeroDomesatual];


// 4 - EXTRAINDO O ANO ATUAL COM 4 DÍGITOS

const anoAtual = new Date ();
const valorDoanoatual = anoAtual.getFullYear();