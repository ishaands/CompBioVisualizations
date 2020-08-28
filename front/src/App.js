import React from "react";
import "./App.css";
import Anime from "react-anime";
import Grid from "@material-ui/core/Grid";
function App() {
	const firstDna = "ATTAG".split("");
	const secondDna = "ATGAG".split("");
	const arrayFirst = firstDna.map((val, key) => {
		return (
			<span style={{ color: "grey" }} key={key}>
				{val}
			</span>
		);
	});
	const arraySecond = secondDna.map((val, key) => {
		return (
			<span style={{ color: "grey" }} key={key}>
				{val}
			</span>
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
				<span style={match} key={`first${i}`}>
					{firstDna[i]}
				</span>
			);

			const animatedSecond = (
				<span style={match} key={`second${i}`}>
					{secondDna[i]}
				</span>
			);
			finalLettersFirst.push(animatedFirst);
			finalLettersSecond.push(animatedSecond);
			setFirstDna(finalLettersFirst);
			setSecondDna(finalLettersSecond);
		};
		for (let i = 0; i < firstLetters.length; i += 1) {
			determineMatch(i);
		}
	};

	return (
		<div className="App">
			<Grid container>
				<Grid item xs={12}>
					<div>{firstLetters}</div>
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
