import React, {useState} from 'react'
import Grid from "@material-ui/core/Grid";
import { motion, AnimatePresence } from "framer-motion";
import Typography from "@material-ui/core/Typography";

function LongestSubstring() {
    //getting the longest shared substring from the beginning, using it with setting state kinda messed up
    const a = "ABCDEFGHIJK";
    const b = "AABDKJFDEFGHIASDF";
    const shared = LongestSharedSubstringIndex(AllSubstrings(a), AllSubstrings(b))

    //Setting states to nothing, can be updated with button press (not sure if there's a better way to do this)
    const [aSub, showaSub] = useState(" ");
    const [bSub, showbSub] = useState(" ");
    const [str, setStr] = useState(" ");


    return (
		<div>
            String a: {a} <br />
            String b: {b} <br /> <br />
            <p>
            Substings A: {aSub} <br /> <br />
            Substings B: {bSub}
            </p>
            <button onClick = {() =>{
                 showaSub(AllSubstrings(a).join(" "))
                 showbSub(AllSubstrings(b).join(" "))
                 }}>show substrings</button>
                 
			{/* {aSub.join(" ")} <br /> <br />
			{bSub.join(" ")} <br /> <br /> */}
            <button onClick = {() => setStr(shared[0])}>click</button>
            <p>Longest shared Substring: {str}</p>
		</div>
	);
}



//LongestSharedSubstring takes a longer and shorter string array and returns the longest substring, as well as the indices of the longest shared substring on each array, respectively. (n^2 time)
function LongestSharedSubstringIndex(arr1,arr2){
    var longestString = [];
    var found = false;

    for (var i = 0; i <= arr2.length; i++){
        for (var j = 0; j <= arr1.length; j++){
            if(arr2[i] == arr1[j]){
                longestString.push(arr2[i]);
                longestString.push(j);
                longestString.push(i);
                return longestString
            }
        }
    }
    return longestString;
}



//Returns all substrings of a string with no repeats
function AllSubstrings(str){
    let arr = [];
    for (var i = 0; i < str.length; i++){
        for (var j = i + 1; j <= str.length; j++){
            let currentSub = str.substring(i,j);
            if (arr.includes(currentSub) == false){
                arr.push(currentSub);
            }
        }
    }
    arr.sort((a,b) => b.length - a.length);
    return arr;
}



export default LongestSubstring
