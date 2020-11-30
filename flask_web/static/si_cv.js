
let buttons = document.querySelectorAll(".accordion");
//let acc_group = new AccordionGroup(buttons);

for (let i=0; i<buttons.length;i++){
    buttons[i].onclick = function(){

        takeTime(this.getAttribute("id")); //take timstamp when clicked

        
        

        
        let prev_active = document.querySelector("button.active.accordion"); //get previously active
        //prev_active.classList.remove("active");

        if (prev_active !== this && prev_active !== null){
            takeTime(prev_active.getAttribute("id")); //take timestamp of previously active if any
        }


        

        swap(prev_active, this); //change display
        


    }
}




let a1 = [];
let w1 = [];
let s1 =[];
let e1 = [];
let ach1 = [];





function takeTime(id){

    let s = new Date();
    switch (id){
      case "about":
        a1.push(s.getTime());
        break;
      case "work":
        w1.push(s.getTime());
        break;
      case "ski":
        s1.push(s.getTime());
        break;
      case "edu":
        e1.push(s.getTime());
        break;
      case "ach":
        ach1.push(s.getTime());
        break;
    }
  
  }








  function totalTimes(){
    let allTimes = [a1, w1, s1, e1, ach1];
  
    
  
    let t = new Date();   //time when finished
    let allTimeTotals = [];   //array of total times spent
    for(let i=0; i<allTimes.length ; i++){
      
      let acc = 0;   //accumulated time
  
      if (allTimes[i].length % 2 == 0 ){            //even number of elements
        
        
        
        for(let j=0; j<allTimes[i].length ; j+=2){
          
          acc +=  allTimes[i][j+1] - allTimes[i][j];   // difference in start and finish times
        }
        allTimeTotals.push(acc);                        //add the accumulated time to array
        
      }
      else{                                             //odd number of elements
        
  
        
        let endTime = t.getTime();
        for(let k=0; k<allTimes[i].length ; k+=2){
          if (k == allTimes[i].length -1){
            acc += endTime - allTimes[i][k];
          }
          else{
            acc += allTimes[i][k+1] - allTimes[i][k];   // difference in start and finish times
          }
        }
        allTimeTotals.push(acc);  //add the accumulated time to array
      }
  
  }
  
  return allTimeTotals;
  }






function summary(){
  
    let times = totalTimes();
    document.querySelector("#a").innerHTML = readingSpeed( countWords(document.getElementById("ab").textContent) ,times[0]);
    document.querySelector("#w").innerHTML = readingSpeed( countWords(document.getElementById("wo").textContent) ,times[1]);
    document.querySelector("#s").innerHTML = readingSpeed( countWords(document.getElementById("sk").textContent) ,times[2]);
    document.querySelector("#e").innerHTML = readingSpeed( countWords(document.getElementById("ed").textContent) ,times[3]);
    document.querySelector("#aa").innerHTML = readingSpeed( countWords(document.getElementById("ac").textContent) ,times[4]);

    document.querySelector("#av").innerHTML = averageSpeed(times) + ext(averageSpeed(times));
    document.querySelector("#metrics").style.display="block";
    document.querySelector("#summary").innerHTML = "Update your speeds"
  }


function getPanel(el){
    switch (el.getAttribute("id")){
        case "about":
            return document.querySelector("#ab");
            
        case "work":
            return document.querySelector("#wo");
        
        case "ski":
            return document.querySelector("#sk");
            
        case "edu":
            return document.querySelector("#ed");
            
        case "ach":
            return document.querySelector("#ac");
            
    }
}

function countWords(wordStr){
  return wordStr.split(" ").length;
}


function swap(from, to){
  
  if(document.getElementById("in") != null){
  var rem = document.getElementById("in");
  rem.parentNode.removeChild(rem);
  }
    
    to.classList.add("active");
    if (from !== null){
        from.classList.remove("active");
        getPanel(from).style.display ="none";
    }
    if(from !== to){
      getPanel(to).style.display = "block";
    }
    
}

function readingSpeed(numwords, timems){
  let wpm = Math.round(numwords/(timems/60000));
  let ex = ext(wpm);
  if (wpm === Infinity){
        return ex;}
  else{
    return wpm + ex;
  }
   //return wpm
}

function readingSpeedA(numwords, timems){
  let wpm = Math.round(numwords/(timems/60000));
  if (wpm== Infinity){
    return 0;
  }
  return wpm;
   //return wpm
}



function readingSpeed200(timems){
  return 200/(timems/60000); //return wpm for 200 words

}

function averageSpeed(times){
  let readingSpeeds = [readingSpeedA( countWords(document.getElementById("ab").textContent) ,times[0]),
  readingSpeedA( countWords(document.getElementById("wo").textContent) ,times[1]),
  readingSpeedA( countWords(document.getElementById("sk").textContent) ,times[2]),
  readingSpeedA( countWords(document.getElementById("ed").textContent) ,times[3]),
  readingSpeedA( countWords(document.getElementById("ac").textContent) ,times[4])];
  let t = 0;
  let l = 0;
  for (let i=0;i<readingSpeeds.length;i++){
    if (readingSpeeds[i] > 0){
      t += readingSpeeds[i];
      l += 1;
    }
  }


  return Math.round(t/l); //return rounded average of speeds that were read

}

function ext(wpm){ 
  if (wpm == Infinity | wpm == Infinity){
    return "Please read section.";
  }
  else{
    return " wpm."
  }
}
