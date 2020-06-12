/*

    WIP : BOOLEANS AND IDS NEED TO BE DISBALED
    
    DOOM-ML SECTOR Training :
    
    This file contains all of the processes or SideDef training
*/

//Taken from Mozilla Foundation, simple function to get a random Int if needed
function getRandomInt(max) {
    return Math.floor(Math.random() * Math.floor(max));
  }
  
  //ML5 Options - Use this to modify the training of the neural network
  const options = {
      inputs: 3,
      outputs: 8,
      task: 'regression',
      debug: 'true',
      epochs: 8
  }
  
  //Specifying the number of inputs and outputs for the VERTEX Object
  const neuralNetwork = ml5.neuralNetwork(options)
  
  //data contains the vertex points, the points contain the data points of the image
  const xs = points["points"]
  const ys = data["sectors"]
  
  //Storing Data here
  let resultData = [];
  
  //Used for fixing duplicate data in arrays. Did not TOUCH
  let incrementer = 0;
  
  function loadData(){
      /*
          This function allows us to load ALL of the vertex Datasets we have available
      */
  }
  
  
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
  
              //Predicting data
            neuralNetwork.predict([pointX,pointY], 
            (err, results) => {
                if(err)
                    {
                        console.log(err)
                    }
                else {
                //Reformatting the ML5 Network result to make it play nice with JSON formatting
                    console.log(results)
                                          }
              });
                  }
              
      
          }
  
  
  //KEEP EMPTY (for now)
  function setup() {
  }
  function draw() {
  }
  
  
  
  
  function mousePressed() {
  ////   neuralNetwork.save()
  //    JSONversion = JSON.stringify(resultData)
  //    console.log(JSONversion)
     DatasetCreation()
  }
  
   //NOT IN USE RIGHT NOW 
  function DatasetCreation()
  {
      for (let i = 0; i < xs.length; i++) {
      //Configuring the data for ML5 Neural Network loading
      const pointX = xs[i].x
      const pointY = xs[i].y
  
      //To stop duplicate values
      for (let j = 0; j < ys.length; j++) {
          
        const dataHeightfloor = ys[j].heightfloor;
        const dataHeightceiling = ys[j].heightceiling;

          const dataTexturefloor = ys[j].texturefloor;
          const dataTextureceiling = ys[j].textureceiling;
          const dataType = ys[j].type;
          const dataId = ys[j].id;
          const dataLightlevel = ys[j].lightlevel;
          //Fixing a potenial dataset problem;
          let dropactors;
          if(ys[j].dropactors == true){
              dropactors = true;
          }
          else
          {
              dropactors = false;
          }


          if (incrementer < ys.length) {
              incrementer++
          } else {
              incrementer = 0;
              neuralNetwork.data.addData([pointX, pointY], [dataHeightfloor,dataHeightceiling,
                dataTexturefloor,dataTextureceiling,
                dataType, dataId,dataLightlevel,dropactors])
          }
          if(i == xs.length-1)
              {
                  //A way to check if the data has been added
                  console.log("DataAdded")
              }
      }
  }
  
  }
  