import React from "react";

const Nucleotide = (props) => {
	const [status, setStatus] = React.useState({ color: "grey" });
	// const changeColor = (color) => {
	// 	setStatus({color: "grey"})
	// };
	return <span style={props.style}>{props.letter}</span>;
};

export default Nucleotide;
