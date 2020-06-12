/*
    DOOM-ML Vertex Training :
    
    This file contains all of the processes necessairly to create vertex data for a UDMF DOOM MAP
    
    
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
    dataUrl:'COMBINEDDATAFINAL2.csv',
    inputs: ["v1x","v1y","v2x","v2y"],
    outputs: ["isCorrect"],
    task: 'regression'
}

//Declare Neural Network
const neuralNetwork = ml5.neuralNetwork(options)


//Storing Data here
let resultData = [];

let pointXArr = []
let pointYArr = []
let colorArr = []

function loadData(){
    
}

const xs = points["points"]


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
        for(let i = 0; i < xs.length; i++)
        { 
            let highestValue = 0;

            shuffle(xs)
for(let j = 0; j < 30; j++)
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
    if(result[0].value > 0.3) {
        resultData.push({"id": 10 ,
                        "v1": i,
                        "v2":j,
                        "con" : result[0].value})
    }
}

                }
            
            //Checking progress of Classifying
            console.log(i,xs.length)

            console.log(highestValue)
        }
        console.log(resultData)
}
            

// KEEP EMPTY DO NOT TOUCH
// They need to be declared but nothing needs to be in them for now
function setup(){
}
function draw(){ 
}


function mousePressed() {
    
}



