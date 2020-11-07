import React from "react";

function Nucleotide({ letter, active }) {
	const activeColor = active === "green" ? "green" : "red";
	return <div style={{ display: "inline", color: activeColor }}>{letter}</div>;
}

export default Nucleotide;
