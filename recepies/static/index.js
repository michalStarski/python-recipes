const ingredients = [];
const steps = [];
let id;

let data;

$(document).ready(function(){

    //Display steps and ingredients 
    function display(){
        //First clear previous view
        $('#ingredients').empty();
        $('#steps').empty();

        //Append again
        ingredients.forEach(e => {
            $('#ingredients').append($('<li>').text(e));
        });

        steps.forEach(e => {
            $('#steps').append($('<li>').text(e));
        })
    }

    function sendData(data){
        $.ajax({
            url         : "/recipe/api/new",
            type        : "post", 
            contentType : 'aplication/json',
            dataType    : 'json',
            data: data
        })
        .done(response => {
            alert("Successfully added a dish!");
            location.replace(`${response.id}`)
        })
    }

    //Add ingredient to an array
    $('#ingBtn').click(function(event){
        event.preventDefault();
        console.log($('#ing').val().trim());
        if($('#ing').val().trim() !== ''){
            ingredients.push($('#ing').val());
        }
        $('#ing').val('');
        display();
    });
    //Add step to an array
    $('#stepBtn').click(function(event){
        event.preventDefault();
        console.log($('#step').val().trim());
        if($('#step').val().trim() !== ''){
            steps.push($('#step').val());
        }
        $('#step').val('');
        display();
    });

    //Create proper json and send data
    $('#submit').click(function(event){
        event.preventDefault();
        if($('#name').val() === '')
            return
        data = new Object();
        data.name = $('#name').val();
        data.photo = $('#photo').val();
        data.ingredients = ingredients;
        data.steps = steps;
        if(data !== undefined)
            sendData(JSON.stringify(data));
    })
});