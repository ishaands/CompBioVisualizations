import React from "react";
import "./App.css";
import Grid from "@material-ui/core/Grid";
import ReactAnime from "react-animejs";

function App() {
	const { Anime, stagger } = ReactAnime;
	console.log(stagger);
	const firstDna = "ATTAGATTTAAAATTAAGGGCAGATA".split("");
	const secondDna = "ATGAGTTATTAATTGCTATATCAGGA".split("");
	const arrayFirst = firstDna.map((val, key) => {
		return (
			<Anime style={{ display: "inline" }}>
				<span style={{ color: "grey" }} key={key}>
					{val}
				</span>
			</Anime>
		);
	});
	const arraySecond = secondDna.map((val, key) => {
		return (
			<Anime style={{ display: "inline" }}>
				<span style={{ color: "grey" }} key={key}>
					{val}
				</span>
			</Anime>
		);
	});
	const [firstLetters, setFirstDna] = React.useState(arrayFirst);
	const [secondLetters, setSecondDna] = React.useState(arraySecond);
	const simulateHamming = () => {
		const correct = { color: "green" };
		const error = { color: "red" };
		const finalLettersFirst = [];
		const finalLettersSecond = [];
		const determineMatch = (i) => {
			let match = firstDna[i] === secondDna[i] ? correct : error;
			const animatedFirst = (
				<Anime
					initial={[{
						targets: "#nucleotide",
						// delay: stagger("100"),
						translateX: 100,
						easing: "linear"
					}]}
					style={{ display: "inline" }}
				>
					<span id="nucleotide" style={match} key={`first${i}`}>
						{firstDna[i]}
					</span>
				</Anime>
			);

			const animatedSecond = (
				<Anime style={{ display: "inline" }}>
					<span style={match} key={`second${i}`}>
						{secondDna[i]}
					</span>
				</Anime>
			);
			finalLettersFirst.push(animatedFirst);
			finalLettersSecond.push(animatedSecond);
		};
		for (let i = 0; i < firstLetters.length; i += 1) {
			setTimeout(determineMatch(i), 1);
			setFirstDna(finalLettersFirst);
			setSecondDna(finalLettersSecond);
			console.log(finalLettersFirst);
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
						{firstLetters}
					</div>
				</Grid>
				<Grid item xs={12}>
					{secondLetters}
				</Grid>
			</Grid>
			<Grid item xs={12}>
				<button onClick={simulateHamming}>Simulate Algorithm</button>
			</Grid>
		</div>
	);
}

export default App;
