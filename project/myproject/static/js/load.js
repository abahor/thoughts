var main = document.getElementById('main')
var sentinel = document.getElementById('sentinel')
var sad = 0
function loadItem() {
  var d = new XMLHttpRequest();
  d.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      if (!this.responseText){
        sentinel.innerHTML = 'No more posts';
        return;
        } else {
          console.log(this.responseText);
          var rererer = document.createElement('div');
          rererer.innerHTML= this.responseText
          main.appendChild(rererer)
          sad += 10
          return ;
        }
      }
    }
  d.open('POST','/load?c='+ sad)
  d.send()
}



var intersectionObserver = new IntersectionObserver(entries => {
  if (entries[0].intersectionRatio <= 0){
    return;
  }
  console.log('working');
  loadItem();
});

intersectionObserver.observe(sentinel);
