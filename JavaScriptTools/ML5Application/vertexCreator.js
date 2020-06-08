/*
    DOOM-ML Vertex Training :
    
    This file contains all of the processes necessairly to create vertex data for a UDMF DOOM MAP
    
    
*/


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
    createVertexData()
}
//Callback when training is complete
function createVertexData(){
        for(let i = 0; i < 475; i++)
        { 
            shuffle(xsX)
            for(let j = 0; j < 100; j++)
                {
                                //Calls back handle results
                let results = neuralNetwork.classify([xsX[i].x ,xsX[i].y , xsX[j].x  , xsX[j].y],handleResults)

                function handleResults(error,result)
                {
                    if(error){
                      console.error(error);
                      return;
                    }
                        if(result[1].confidence > 0.45)
                        {
                            //Grabs the index
                            resultData.push({id : "0", v1: i, v2: j, confidence : result[1].confidence})
                        }
                
                }



                }
            
            //Checking progress of Classifying
            console.log(i,475)


        }
        console.log(resultData)
}
            


function setup(){
}
function draw(){ 
}


function mousePressed() {
    
}



