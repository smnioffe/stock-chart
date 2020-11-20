
//URL Paramter Sniffer

	$.urlParam = function(name){
    var results = new RegExp('[\?&]' + name + '=([^&#]*)').exec(window.location.href);
    if (results==null){
       return null;
    }
    else{
       return results[1] || 0;
    }
}
//example:  index.html?error=yes    -->   console.log($.urlParam('error')) : yes


	  
//force two digit with paddied 0.  ex 5-> 05
           function pad(n) {
          return (n < 10) ? ("0" + n) : n;
      };  
	  
//convertm minutes to HHMM
      function convertToHHMM(info) {
        var hrs = parseInt(Number(info));
        var min = Math.round((Number(info)-hrs) * 60);

        return hrs+':'+pad(min);
      }

//format number with commas
function numberWithCommas(x) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

//date of the week
Date.prototype.getWeekDay = function() {
    var weekday = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
    return weekday[this.getDay()];
}

//convert thisExampleText to this Example Text
function splitWithSpace(str){
return str.replace(/([a-z])([A-Z])/g, '$1 $2').replace('Or','or')
}

//title case
function toTitleCase(str) {
    return str.replace(
        /\w\S*/g,
        function(txt) {
            return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();
        }
    );
}

function roundNumber(num, scale) {
  if(!("" + num).includes("e")) {
    return +(Math.round(num + "e+" + scale)  + "e-" + scale);
  } else {
    var arr = ("" + num).split("e");
    var sig = ""
    if(+arr[1] + scale > 0) {
      sig = "+";
    }
    return +(Math.round(+arr[0] + "e" + sig + (+arr[1] + scale)) + "e-" + scale);
  }
}


function capitalizeFirstLetter(string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
}


function isNumeric(n) {
  return !isNaN(parseFloat(n)) && isFinite(n);
}


       
function isEven(n) {
  return n == parseFloat(n)? !(n%2) : void 0;
}


//Example Lighten:
//shadeColor("#63C6FF",40);
//Example Darken:
//shadeColor("#63C6FF",-40);
function shadeColor(color, percent) {

    var R = parseInt(color.substring(1,3),16);
    var G = parseInt(color.substring(3,5),16);
    var B = parseInt(color.substring(5,7),16);

    R = parseInt(R * (100 + percent) / 100);
    G = parseInt(G * (100 + percent) / 100);
    B = parseInt(B * (100 + percent) / 100);

    R = (R<255)?R:255;  
    G = (G<255)?G:255;  
    B = (B<255)?B:255;  

    var RR = ((R.toString(16).length==1)?"0"+R.toString(16):R.toString(16));
    var GG = ((G.toString(16).length==1)?"0"+G.toString(16):G.toString(16));
    var BB = ((B.toString(16).length==1)?"0"+B.toString(16):B.toString(16));

    return "#"+RR+GG+BB;
}



        function rgbToHex(col) {
            if (col.charAt(0) == 'r') {
                col = col.replace('rgb(', '').replace(')', '').split(',');
                var r = parseInt(col[0], 10).toString(16);
                var g = parseInt(col[1], 10).toString(16);
                var b = parseInt(col[2], 10).toString(16);
                r = r.length == 1 ? '0' + r : r;
                g = g.length == 1 ? '0' + g : g;
                b = b.length == 1 ? '0' + b : b;
                var colHex = '#' + r + g + b;
                return colHex;
            }
        }

//var arr = [ 'A', 'B', 'D', 'E' ];
//arr.insert(2, 'C');
// arr == [ 'A', 'B', 'C', 'D', 'E' ]
Array.prototype.insert = function ( index, item ) {
    this.splice( index, 0, item );
};


//remove value from array
function removeArr(array, element) {
    const index = array.indexOf(element);
    
    if (index !== -1) {
        array.splice(index, 1);
    }
return array
	}
	
//Get position of Nth instance of a string
//var string = "XYZ 123 ABC 456 ABC 789 ABC";
///getPosition(string, 'ABC', 2)
function getPosition(string, subString, index) {
   return string.split(subString, index).join(subString).length;
}




	
// re-order d3 SVGs
 // https://github.com/wbkd/d3-extended
    d3.selection.prototype.moveToFront = function() {  
      return this.each(function(){
        this.parentNode.appendChild(this);
      });
    };
    d3.selection.prototype.moveToBack = function() {  
        return this.each(function() { 
            var firstChild = this.parentNode.firstChild; 
            if (firstChild) { 
                this.parentNode.insertBefore(this, firstChild); 
            } 
        });
    };