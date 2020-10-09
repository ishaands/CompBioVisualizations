import React from "react";
import { motion } from "framer-motion";
// state vars representing the future substring arrays

const TestKmers = (props) => {
	const [substringsOne, setSubstringsOne] = React.useState([]);
	const [substringsTwo, setSubstringsTwo] = React.useState([]);
	const [index, setIndex] = React.useState(0);
	// state vars representing the two input strings
	const [dnaOne, setDnaOne] = React.useState("ATTAG");
	const [dnaTwo, setDnaTwo] = React.useState("ATTAG");
	// create a list of button elems that represent the "steps" of the algorithm
	// const algoButtons = []
	// function to be fired once user clicks on the startAlgo button
	const startAlgo = () => {
		// dummy substrings that mimic fetching from the backend
		setSubstringsOne(["ATT", "TTA", "TAG"]);
		setSubstringsTwo(["ATT", "TTA", "TAG"]);
		incrementIndex();
	};

	// function to be fired once substrings have been displayed and user wants to match them

	const matchSubs = () => {
		// get match data from backend
		incrementIndex();
	};
	const algoButtons = [
		<button id="startAlgo" onClick={startAlgo}>
			Start Algorithm
		</button>,
		<button id="matchSubs" onClick={matchSubs}>
			Match Substrings
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
				{substringsOne.map((val, key) => {
					return (
						<motion.h3
							initial={{ opacity: 0 }}
							animate={{ opacity: 1 }}
							transition={{ duration: 1, delay: 1 * key }}
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
							transition={{ duration: 1, delay: 1 * key }}
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
