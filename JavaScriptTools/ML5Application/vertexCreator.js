/*
    DOOM-ML Vertex Training :
    
    This file contains all of the processes necessairly to create vertex data for a UDMF DOOM MAP
    
    
*/

//Taken from Mozilla Foundation : 
function getRandomInt(max) {
  return Math.floor(Math.random() * Math.floor(max));
}


const options = {
    dataUrl:'CATWALKLINEDEFTest.csv',
    inputs: ["v1x","v1y","v2x","v2y"],
    outputs: ["isCorrect"],
    task: 'classification',
    debug: 'true',
    epochs: 100,
    batchSize : 64,
    learningRate : 0.1
}

//Specifying the number of inputs and outputs for the VERTEX Object
const neuralNetwork = ml5.neuralNetwork(options)


//Storing Data here
let resultData = [];

//Used for fixing duplicate data in arrays. Did not TOUCH
let incrementer = 0;

let pointXArr = []
let pointYArr = []
let colorArr = []

function loadData(){
    
}

const xsX = points[0]["X"]
const xsY = points[0]["Y"]

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

function nnTrain(){
    //Normalises the data from a scale from 0 to 1
    //CreateVertexData is a CALLBACK

    neuralNetwork.train(createVertexData);
}

let iCon;
let jCon;

//Callback when training is complete
function createVertexData(){
    console.log(xsX[0])
    console.log("Vertex is here 1")
        for(let i = 0; i < Object.keys(xsX).length; i++)
        { 
            for(let j = 0; j < Object.keys(xsX).length; j++)
                {
            //Calls back handle results
            neuralNetwork.classify([xsX[i] ,xsY[i] , xsX[j]  , xsY[j]] , handleResults)
                }


        }
                        }
            
function handleResults(error,result)
{
        if(error){
      console.error(error);
      return;
    }
    console.log(result[1].confidence)
}

//KEEP EMPTY
function setup() {

}
function draw() {
}

function mousePressed() {
    console.log(resultData)

}



