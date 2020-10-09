import React, { useState, useEffect } from "react";
import Nucleotide from "./Nucleotide";

export default function SharedKmers() {
	const firstDna = "ACTG";
	const secondDna = "ATGC";

	const [listNucsA, setListNucsA] = useState(
		firstDna.split("").map((v, k) => {
			return <Nucleotide key={k} active="green" letter={v} />;
		})
	);
	const [listNucsB, setListNucsB] = useState(
		secondDna.split("").map((v, k) => {
			return <Nucleotide key={k} active="green" letter={v} />;
		})
	);

	const simulateSharedKmers = () => {
		const myLoop = (i) => {
			setTimeout(() => {
				setListNucsA((prevState) => {
					prevState + "z"
				}
					);
				console.log("Hi");
				if (i < firstDna.length) {
					myLoop(i + 1);
				}
			}, 1000);
		};
		myLoop(0);
	};

	return (
		<div>
			{listNucsA} {listNucsB}
			<button onClick={simulateSharedKmers}>Simulate Algorithm</button>
		</div>
	);
}
