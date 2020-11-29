import React from "react";
import { motion } from "framer-motion";
const axios = require("axios");
const TestKmers = (props) => {
	// this is for the first stage of the algorithm, where substrings get loaded in from backend
	const [substringsOne, setSubstringsOne] = React.useState([]);
	const [substringsTwo, setSubstringsTwo] = React.useState([]);
	const baseUrl = "/lss";
	// state variable representing the current algorithm
	const [index, setIndex] = React.useState(0);

	// state vars representing the two input strings
	const [dnaOne, setDnaOne] = React.useState("ATTAG");
	const [dnaTwo, setDnaTwo] = React.useState("ATTGA");

	const [matchedSubstrings, setMatchedSubstrings] = React.useState([]);

	const [longestSubString, setLongestSubstring] = React.useState("");
	// function to be fired once user clicks on the startAlgo button
	const startAlgo = () => {
		// dummy substrings that mimic fetching from the backend
		// making official axios post request to flask backend
		axios
			.post(`/lss-findsubstrings`, { str1: dnaOne, str2: dnaTwo })
			.then((res) => {
				const data = res.data;
				setSubstringsOne(data["str1"]);
				setSubstringsTwo(data["str2"]);
				incrementIndex();
			});
	};

	// function to be fired once substrings have been displayed and user wants to match them

	const matchSubs = () => {
		// get match data from backend
		incrementIndex();
		setSubstringsOne([]);
		setSubstringsTwo([]);
		axios
			.post(`${baseUrl}-findshared`, {
				list1: substringsOne,
				list2: substringsTwo,
			})
			.then((res) => {
				const data = res.data;
				setMatchedSubstrings(data["shared-substrings"]);
				incrementIndex();
			});
	};

	// function to be fired once matching substrings have been displayed and user wants to get the longest one
	const longestSub = () => {
		// get longest data from backend
		incrementIndex();
		setMatchedSubstrings([]);
		axios.post(`${baseUrl}`, { list: matchedSubstrings }).then((res) => {
			const data = res.data;
			setLongestSubstring(data["longest-shared-substring"]);
			incrementIndex();
		});
	};
	// create a list of buttons that will initiate a given algorithm stage
	const algoButtons = [
		<button id="startAlgo" onClick={startAlgo}>
			Start Algorithm
		</button>,
		<button id="matchSubs" onClick={matchSubs}>
			Match Substrings
		</button>,
		<button id="longestSub" onClick={longestSub}>
			Get Longest Substring
		</button>,
		<button style={{ visbility: "none" }}></button>,
	];

	const incrementIndex = () => {
		if (index !== algoButtons.length) {
			setIndex(index + 1);
		}
	};

	return (
		<div>
			<h1>DNA One: {dnaOne}</h1>
			<h1>DNA Two: {dnaTwo}</h1>
			<div>
				{longestSubString && (
					<motion.h3
						initial={{ opacity: 0 }}
						animate={{ opacity: 1, color: "#50c878" }}
						transition={{ duration: 1, delay: 0.5 }}
						style={{ display: "inline" }}
					>
						{longestSubString}
					</motion.h3>
				)}
				{matchedSubstrings.map((val, key) => {
					return (
						<motion.h3
							initial={{ opacity: 0 }}
							animate={{ opacity: 1, color: "#50c878" }}
							transition={{ duration: 1, delay: 0.5 * key }}
							style={{ display: "inline" }}
							key={key}
						>
							{val}{" "}
						</motion.h3>
					);
				})}
				{substringsOne.map((val, key) => {
					return (
						<motion.h3
							initial={{ opacity: 0 }}
							animate={{ opacity: 1 }}
							transition={{ duration: 1, delay: 0.5 * key }}
							style={{ display: "inline" }}
							key={key}
						>
							{val}{" "}
						</motion.h3>
					);
				})}
			</div>
			<div>
				{substringsTwo.map((val, key) => {
					return (
						<motion.h3
							initial={{ opacity: 0 }}
							animate={{ opacity: 1 }}
							transition={{ duration: 1, delay: 0.5 * key }}
							style={{ display: "inline" }}
							key={key}
						>
							{val}{" "}
						</motion.h3>
					);
				})}
			</div>
			{algoButtons[index]}
		</div>
	);
};

export default TestKmers;
