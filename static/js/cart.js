console.log('hello world')

var updatedBtns = document.getElementsByClassName('update-cart')
// get all the Update Cart btn

for (var i = 0;i<updatedBtns.length; i++){//go through each btn
    updatedBtns[i].addEventListener('click',function (){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productID:', productId,'Action:',action)// check in console

        console.log('USER:',user)
        if(user === 'AnonymousUser'){
           console.log('user is not loged in')
        }else{
            console.log('user is authenticated, sending data...',user)
        }

    })


}