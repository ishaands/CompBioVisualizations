import React from "react";
import { motion, AnimatePresence } from "framer-motion";
import Grid from "@material-ui/core/Grid";
import Typography from "@material-ui/core/Typography";
import "../styles/Hamming.css";
export default function Hamming() {
	const firstDna = "ATTAGATTTAAAATTAAGGGCAGATA".split("");
	const secondDna = "ATGAGTTATTAATTGCTATATCAGGA".split("");
	const arrayFirst = firstDna.map((val, key) => {
		return (
			<AnimatePresence>
				<motion.span
					style={{ display: "inline" }}
					initial={{ opacity: 0, color: "#777777" }}
					animate={{ opacity: 1 }}
					transition={{ duration: 1, delay: 0.1 * key }}
					exit={{ opacity: 0 }}
					key={key}
					className={"nucleotide"}
				>
					{val}
				</motion.span>
			</AnimatePresence>
		);
	});
	const arraySecond = secondDna.map((val, key) => {
		return (
			<AnimatePresence>
				<motion.span
					style={{ display: "inline" }}
					initial={{ opacity: 0, color: "#777777" }}
					animate={{ opacity: 1 }}
					transition={{ duration: 1, delay: 0.1 * key }}
					exit={{ opacity: 0 }}
					key={key}
					className={"nucleotide"}
				>
					{val}
				</motion.span>
			</AnimatePresence>
		);
	});

	const [firstLetters, setFirstDna] = React.useState(arrayFirst);
	const [secondLetters, setSecondDna] = React.useState(arraySecond);
	const simulateHamming = () => {
		const correct = "#38C95D";
		const error = "#D62121";

		const finalLettersSecond = [];

		const determineMatch = (i) => {
			let match = firstDna[i] === secondDna[i] ? correct : error;
			const animatedFirst = (
				<motion.span
					initial={{
						color: "#777777",
					}}
					id={"hi"}
					animate={{ color: match }}
					transition={{ duration: 0.1, delay: 0.1 * i }}
					key={`first${i}`}
					className={"nucleotide"}
				>
					{firstDna[i]}
				</motion.span>
			);

			const animatedSecond = (
				<motion.span
					initial={{
						opacity: 0,
						color: "#777777",
					}}
					animate={{ opacity: 1, color: match }}
					transition={{ duration: 1, delay: 0.1 * i }}
					key={`second${i}`}
					className={"nucleotide"}
				>
					{firstDna[i]}
				</motion.span>
			);

			// finalLettersFirst.push(animatedFirst);
			// finalLettersSecond.push(animatedSecond);
			firstLetters.splice(i, 1, animatedFirst);
			secondLetters.splice(i, 1, animatedSecond);
			const finalLettersFirst = firstLetters;
			setFirstDna(finalLettersFirst);
			const finalLettersSecond = secondLetters;
			setSecondDna(finalLettersSecond);
			console.log(firstLetters);
		};
		for (let i = 0; i < firstLetters.length; i += 1) {
			determineMatch(i);
		}
	};

	return (
		<div className="App">
			<Grid container>
				<Grid item xs={12}>
					<div
						style={{
							whiteSpace: "nowrap",
							overflowX: "auto",
						}}
					>
						<Typography style={{ display: "inline" }} variant={"h6"}>
							String A
						</Typography>{" "}
						{firstLetters}
					</div>
				</Grid>

				<Grid item xs={12}>
					<Typography
						style={{ display: "inline" }}
						className={"string"}
						variant={"h6"}
					>
						String B
					</Typography>{" "}
					{secondLetters}
				</Grid>
			</Grid>
			<Grid item xs={12}>
				<button onClick={simulateHamming}>Simulate Algorithm</button>
			</Grid>
		</div>
	);
}
