const stats = document.getElementsByTagName('i')
const colecao = document.querySelectorAll(".status")


for (let i = 0; i < colecao.length; i++) {
    
    if(colecao[i].innerHTML == "Alive") {
        stats[i].style.color = 'green'
    }else if (colecao[i].innerHTML == "Dead") {
        stats[i].style.color = 'red'
    }
    else {
        stats[i].style.color = 'gray'
    }
}
