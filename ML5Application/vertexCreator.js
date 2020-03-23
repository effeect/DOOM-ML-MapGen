/*
    DOOM-ML Vertex Training :
    
    This file contains all of the processes necessairly to create vertex data for a UDMF DOOM MAP
    
    
*/

//Taken from Mozilla Foundation : 
function getRandomInt(max) {
  return Math.floor(Math.random() * Math.floor(max));
}


const options = {
    inputs: 2,
    outputs: 2,
    task: 'regression',
    debug: 'true',
    epochs: 160,
    batchSize : 32,
    learningRate : 0.001
}

//Specifying the number of inputs and outputs for the VERTEX Object
const neuralNetwork = ml5.neuralNetwork(options)

//data contains the vertex points, the points contain the data points of the image
const xs = points["points"]
const ys = data["vertices"]

//Storing Data here
let resultData = [];

//Used for fixing duplicate data in arrays. Did not TOUCH
let incrementer = 0;

let pointXArr = []
let pointYArr = []
let colorArr = []

function loadData(){
    /*
        This function allows us to load ALL of the vertex Datasets we have available
    */
    neuralNetwork.loadData('Datasets/CANYON2/ArrayData.json')
    
}
loadData()


function nnTrain(){
    //Normalises the data from a scale from 0 to 1
    neuralNetwork.normalizeData();
    //CreateVertexData is a CALLBACK
    neuralNetwork.train(createVertexData);
}

//Callback when training is complete
function createVertexData(){
    //Using data from another dataset
//    neuralNetwork.save();
        for (let i = 0; i < 10000; i++) 
        {   
            const pointX = xs[i].x;
            const pointY = xs[i].y;
            const color = xs[i].color;
            
            
//            console.log(pointX)
//            console.log(pointY)
//            console.log(color)

            //Predicting data
                    neuralNetwork.predict([pointX,pointY], 
                                  (err, results) => {
                                        if(err)
                                            {
                                                console.log(err)
                                            }
                                        else {
                                                //Reformatting the ML5 Network result to make it play nice with JSON formatting
//                                                console.log(results)

                                                                resultData.push({x : results[0], y : results[1]})
                                                    }
                                        })
            }
                }
            


//KEEP EMPTY
function setup() {
}
function draw() {
}

function mousePressed() {
////   neuralNetwork.save()
//    JSONversion = JSON.stringify(resultData)
//    console.log(JSONversion)
//DatasetCreation()
    
//    for(let i = 0; i < resultData.length; i++)
//        {
//            const stringVersionx = Number(resultData[i].x)
//            const stringVersiony = Number(resultData[i].y)
//            
//            resultData[i].x = stringVersionx
//            resultData[i].y = stringVersiony
//        }
}

//NOT IN USE RIGHT NOW 
function DatasetCreation()
{
    for (let i = 0; i < xs.length; i++) {
    //Configuring the data for ML5 Neural Network loading
    const pointX = xs[i].x
    const pointY = xs[i].y

    const dataX = ys[i].x
    const dataY = ys[i].y

    neuralNetwork.data.addData([pointX, pointY], [dataX, dataY])
        
    }
}


