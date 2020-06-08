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
    task: 'classification'
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

const xsX = points["points"]


function nnTrain(){
    //Normalises the data from a scale from 0 to 1
    //CreateVertexData is a CALLBACK

    neuralNetwork.train(handleData);
}

let iCon;
let jCon;
function handleData(){
    console.log("Training Complete")
}
//Callback when training is complete
function createVertexData(){
        for(let i = 0; i < 460; i++)
        { 
            for(let j = 0; j < 100; j++)
                {
                                //Calls back handle results
                let results = neuralNetwork.classify([xsX[i].x ,xsX[i].y , xsX[j].x  , xsX[j].y])
                resultData.push(results)
                }
            
            //Checking progress of Classifying
            console.log(i,475)


        }
}
            
function handleResults(error,result)
{
    if(error){
      console.error(error);
      return;
    }
    
    console.log(result)

}

function setup(){
nnTrain()
}

function draw(){
    
}


function mousePressed() {
    
    createVertexData()
}



