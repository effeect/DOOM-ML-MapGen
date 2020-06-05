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
    batchSize : 32,
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



function nnTrain(){
    //Normalises the data from a scale from 0 to 1
    //CreateVertexData is a CALLBACK

    neuralNetwork.train(createVertexData);
}

//Callback when training is complete
function createVertexData(){
                    const input = {"v1x" : 1312,"v2x" : 3264, "v2x" : 1344,"v2y" : 3264}
                    
                    neuralNetwork.classify(input,handleResults)
            }
            
function handleResults(error,result)
{
    if(error){
      console.error(error);
      return;
    }
    console.log(result); // {label: 'red', confidence: 0.8};
}

//KEEP EMPTY
function setup() {
}
function draw() {
}

function mousePressed() {
    
    for(let i = 0; i < resultData.length; i++)
        {
            const stringVersionx = Number(resultData[i].x)
            const stringVersiony = Number(resultData[i].y)
            
            resultData[i].x = stringVersionx
            resultData[i].y = stringVersiony
        }
}



