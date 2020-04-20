/* Written by Oliver Dimes, GUOL
    
    PNG JSON DATA creator
    
    I had some issues developing a dataset which contained color values and X and Y coordinates 
    within a clean PNG Image format. So I decided to create my own using some simple JavaScript.
    While this process is a little lengthy and a python program would be a bit more efficent. This
    solution works and it gives us the data as a JSON output which is essential for our needs.
    
    As of right now as of 4/3/2020, you can't download the JSON file, this is a feature I may add in future
 
 Special thanks to :
    - https://stackoverflow.com/questions/53231699/converting-png-to-tensor-tensorflow-js
*/

//Declaring is as an HTML object
imageData = new Image()
imageData.src = 'VIRGIL2.WAD_MAP03.png'
image = imageData

//Line lengths
let dataCoordinates=[];
let lineLength;

let marImage = new MarvinImage();
marImage.load('VIRGIL2.WAD_MAP03.png')

function createImageData()
{
    console.log("Working")
    // https://stackoverflow.com/questions/8751020/how-to-get-a-pixels-x-y-coordinate-color-from-an-image
    //Grabbing HTML elements with MarvinJ
   let x = 710;
   let y = 569;
    
   //A loop to loop through all of the pixels in order to get a dataset
   for(let i = 0; i < x; i++)
       {
        for(let j = 0; j < y; j++)
            {
//                console.log("Searching...")
                let temp = marImage.getAlphaComponent(i,j)
                //Using getAlpha to scan the image and creates a dataset
                if(temp > 0)
                    {
                        //Normalising the Number Values
                        let rangeChangerX = map(i,0,710,-1,1);
                        let rangeChangerY = map(j,0,569,-1,1);
                        
                        let color = marImage.getIntColor(i,j)
                        marImage.getIntColor();
                        dataCoordinates.push({x : rangeChangerX, y : rangeChangerY, color : color });
                    }
            }
       }
    
    for(let i = 0; i < dataCoordinates.length; i++)
        {
            let checker = i+1;
            let tempX = dataCoordinates[i].x;
            let tempY = dataCoordinates[i].y;

            for(let j = 0; j < dataCoordinates.length; j++)
                {
                    if(tempX == dataCoordinates[j].x)
                        {
                            dataCoordinates.splice(j,1);
                        }
                    if(tempY == dataCoordinates[j].y)
                        {
                            dataCoordinates.splice(j,1);
                        }
                }
            
//            if(tempX + lineLength == dataCoordinates[checker].x)
//                {
//                    console.log("trigger")
//                    lineLength++
//                }
//            if(tempX + lineLength!= dataCoordinates[checker].x)
//                {
//                    let length = i - lineLength 
//                    console.log("splice")
//                    dataCoordinates.splice(length,lineLength)
//                    lineLength = 0;
//                }
//            
//            if(tempY + lineLength == dataCoordinates[checker].y)
//                {
//
//                    lineLength++
//                }
//            if(tempY + lineLength != dataCoordinates[checker].y)
//                {
//                    let length = i - lineLength 
//                    dataCoordinates.splice(length,lineLength)
//                    lineLength = 0;
//                }
        }
}

function preload(){
    createImageData()
}

//These functions are needed keep them
function setup(){

}

function draw(){
    
}

function mousePressed(){
    console.log(dataCoordinates)
    JSONversion = JSON.stringify(dataCoordinates)
    console.log(JSONversion)
}