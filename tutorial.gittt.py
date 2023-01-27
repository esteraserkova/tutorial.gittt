<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aplikācija</title>

    <style>
        .poga {
            background-color: coral;
            color: blueviolet;
            width: 50px;
            height: 30px;
        }
    </style>
</head>
<body>
    <h1>Get 10 points to see my favorite music video</h1>  
    
    <div class="js_musicLink"></div> 
    
    <h2>Points <span class="js_result">0</span></h2>

    <button class="poga js_plus">+</button>
    <button class="poga js_minus">-</button>
</body>
<script>
    const plusButton = document.querySelector('.js_plus')
    const ourResult = document.querySelector('.js_result')
    const musicLink = document.querySelector('.js_musicLink')
    const minusButton = document.querySelector('.js_minus')

    let result = 0

    plusButton.addEventListener('click',() => {
        result = result +1
        ourResult.innerHTML = result
        if(result>=10){
            musicLink.innerHTML = `<a href="https://youtu.be/dQw4w9WgXcQ">My favorite music video</a>`
        }
    })

    minusButton.addEventListener('click', () => {
        window.open('https://youtu.be/dQw4w9WgXcQ')
    })
</script>
</html>