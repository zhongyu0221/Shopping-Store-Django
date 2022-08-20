// browser caching JS. shift+f5 to refresh


var user = document.getElementById("myVar").value;
console.log('check user:',user)

var updatedBtns = document.getElementsByClassName('update-cart')
// get all the Update Cart btn

for (var i = 0;i<updatedBtns.length; i++){//go through each btn
    updatedBtns[i].addEventListener('click',function (){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:', productId,'action:',action)// check in console


        console.log('USER:',user)
        if(user === 'AnonymousUser'){
           console.log('user is not loged in')
        }else{
            updateUserOrder(productId,action)
        }
    })
}




function updateUserOrder(productId,action){

    console.log('user is authenticated, sending data...user name',user)

    var url = '/updateitem/' //where we wanna send data to

//to post data, use fetch. Fetch API
    fetch(url,{
        method:'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken//add csrf token in main html
        },
        //body is the part of data we wanna send. send as a string
        body:JSON.stringify({'productId': productId,'action':action})

        })
        //once the data is process, get response
        .then((response) =>{//return json format data
            return response.json()
        })

        .then((data) =>{//return the real data
        console.log('Return Data',data)
            // the data here is form view.py json JsonResponse
            location.reload()
            // reload the page ？
    });

}

function getCookie(name){
    var cookieArr = document.cookie.split(';');
    //split cookie string adn get all individual name = value  pairs

    //loop through the array elements
    for (var = i=0;i<cookieArr.length;i++){
        var cookiePair = cookieArr[i].split('=');

        //remove whitespace at the begining of the cookie name and compare with given string
        if(name == cookiePair[0].trim()){
            return decodeURIComponent(cookiePair[1]);
        }


        return null; //if not found
    )


}