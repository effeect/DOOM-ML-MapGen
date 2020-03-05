/*
    DOOM-ML Vertex Training :
    
    This file contains all of the processes necessairly to create vertex data for a UDMF DOOM MAP
    
    
*/

const options = {
    inputs: 3,
    outputs: 2,
    task: 'regression',
    debug: 'true'
}

//Specifying the number of inputs and outputs for the VERTEX Object
const neuralNetwork = ml5.neuralNetwork(options)

//data contains the vertex points, the points contain the data points of the image
const xs = points["points"]
const ys = data["vertices"]

let resultData = [];

//Used for fixing duplicate data in arrays. Did not TOUCH
let incrementer = 0;


function loadData(){
 
   //Testing Data
    neuralNetwork.loadData('Datasets/BLACKTWR2/BLACKTWR-DATASET.json')
    
}


function nnTrain(){
    //Normalises the data before we can train it 
    neuralNetwork.data.normalize()
    neuralNetwork.train(createVertexData);
}
//Callback when training is complete
function createVertexData(){
    //Using data from another dataset
        for (let i = 0; i < 200; i++) 
        {
            let randomNumber = getRandomInt(xs.length)
            //Configuring the data for ML5 Neural Network loading
            
            const pointX = xs[randomNumber].x;
            const pointY = xs[randomNumber].y;
            const color = xs[randomNumber].color;

            //Predicting data
            neuralNetwork.predict([pointX,pointY,color], 
                                  (err, results) => {
                                        if(err)
                                            {
                                                console.log(err)
                                            }
                                        else {
                                                console.log(results)
                                                resultData.push(results)
                                        }
            });
    
        }
}

loadData()

function setup() {

}

function draw() {
}

function mousePressed() {
//    neuralNetwork.saveData('vertexDataset');
}

 //NOT IN USE RIGHT NOW 
function DatasetCreation()
{
    for (let i = 0; i < xs.length; i++) {
    //Configuring the data for ML5 Neural Network loading
    const pointX = xs[i].x
    const pointY = xs[i].y
    const color = xs[i].color

    //To stop duplicate values
    for (let j = 0; j < ys.length; j++) {
        const dataX = ys[j].x
        const dataY = ys[j].y
        if (incrementer < ys.length) {
            incrementer++
        } else {
            incrementer = 0;
            neuralNetwork.data.addData([pointX, pointY, color], [dataX, dataY])

        }

    }
}

}
