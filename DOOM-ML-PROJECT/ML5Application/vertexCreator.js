/*
    DOOM-ML LINEDEF Training :
    
    This file contains all of the processes necessairly to create LINEDEF Data for DOOM
    
    Please use the following commands to run the program properly :
    
    
    
*/


//Shuffle Array Function
function shuffle(array) {
    var currentIndex = array.length, temporaryValue, randomIndex;
  
    // While there remain elements to shuffle...
    while (0 !== currentIndex) {
  
      // Pick a remaining element...
      randomIndex = Math.floor(Math.random() * currentIndex);
      currentIndex -= 1;
  
      // And swap it with the current element.
      temporaryValue = array[currentIndex];
      array[currentIndex] = array[randomIndex];
      array[randomIndex] = temporaryValue;
    }
  
    return array;
  }

//Options for Neural Network : https://learn.ml5js.org/docs/#/reference/neural-network
const options = {
    dataUrl:'DATASET.csv',
    inputs: ["v1x","v1y","v2x","v2y"],
    outputs: ["isCorrect"],
    task: 'regression'
}

//Declare Neural Network
const neuralNetwork = ml5.neuralNetwork(options)


//Storing Data here
let resultData = [];

//We can load data from this function if needed but since we are loading it within options, it should be okay.
function loadData(){
    
}


const xs = points["points"]

//If you are having WEBGL errors with the image, please consider changing it
let limit = xs.length

function nnTrain(){
    //Normalises the data from a scale from 0 to 1
    //CreateVertexData is a CALLBACK
    neuralNetwork.train(handleData);
   
    
}

function handleData(){
    console.log("Training Complete")
    createVertexData()
}

//Callback when training is complete
function createVertexData(){
        for(let i = 0; i < limit; i++)
        { 
            let highestValue = 0;

            shuffle(xs)
            for(let j = 0; j < 40; j++)
            {
            //Calls back handle results
            let results = neuralNetwork.predict([xs[i].x ,
                                                xs[i].y ,
                                                xs[j].x  , 
                                                xs[j].y],
                                                handleResults)
            function handleResults(error,result)
            {
                if(error){ console.error(error); return; }
                //If the result is above a certain threshold of "confidence", it will be pushed to this array which is can then be transferred to the user
                if(result[0].value > 0.6) {
                    resultData.push({"id": 10 ,
                                    "v1": i,
                                    "v2":j,
                                    "con" : result[0].value})
                }
            }

            }
            
            //Progress bar
            console.log(i,xs.length)

            console.log(highestValue)
        }
        console.log(resultData)
}
            

// KEEP EMPTY DO NOT TOUCH
// They need to be declared but nothing needs to be in them for now
function preload(){
   
}
function setup(){
    
}
function draw(){ 
}


function mousePressed() {
}



