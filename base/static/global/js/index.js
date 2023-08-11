const stats = document.getElementsByClassName("fa-solid")
const title = document.getElementsByClassName("status")


for (let index = 0; index < title.length; index++) {
    
    if (title[index].innerHTML == "Alive") {
        stats[index].className += "green"
    }

}
// title.forEach(element => {
//     if (element.value == "Vivo"){
//         stats[index].className += "green"
//     }
// });
