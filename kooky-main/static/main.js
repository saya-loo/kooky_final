//window.addEventListener("DOMContentLoaded",() => {
// const c = new Switch("#switch");
//});
//
//class Switch {
// constructor(el) {
//  this.el = document.querySelector(el);
//  this.el?.addEventListener("change",this.removePristine);
// }
// removePristine() {
//  this.removeAttribute("data-pristine");
// }
//}
//
//document.getElementById('btn').onclick = function() {
//  let button = document.querySelectorAll('.subject__btn');
//  let main = document.getElementById('subject');
//    if (main.classList.contains('dark')) {
//      main.classList.remove('dark');
//    } else{
//      main.classList.add('dark');
//    }
//}
//
//const list = document.querySelector('.subject__filter'),
//      items = document.querySelectorAll('.subject__item');
//const listItem = document.querySelectorAll('.subject__btn');
//
//
//function filter(){
//  list.addEventListener('click', event => {
//    const targetId = event.target.dataset.id;
//    const target = event.target;
//
//    listItem.forEach(listItem => listItem.classList.remove('active'));
//    target.classList.add('active');
//
//      switch(targetId){
//      case 'all':
//        getItems('subject__item');
//        break;
//      case 'winter':
//
//        getItems(targetId);
//
//        break;
//      case 'autumn':
//
//                getItems(targetId);
//
//        break;
//      case 'summer':
//
//                getItems(targetId);
//
//        break;
//      }
//  });
//
//
//
//}
//filter();
//
//function getItems(className) {
//   items.forEach(item => {
//    if (item.classList.contains(className)) {
//      item.classList.remove('anime');
//    } else{
//      item.classList.add('anime');
//    }
//   });
//}
//
//items.forEach((card) => {
//  card.ontransitionend = function () {
//    if (card.classList.contains('anime')) {
//      card.classList.add('hide');
//    } else{
//      card.classList.remove('hide');
//    }
//  }
//});
//
//
