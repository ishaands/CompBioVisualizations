import React from 'react';
import "../styles/SpeciesRichness.css";

export default function SpeciesRichness() {
    const firstGroup = ["ACT", "ATG", "TTG", "AAG", "TAA"];
    const secondGroup = ["ACT", "ATC", "TTG", "AGG", "TAA"];

    const firstCol = firstGroup.map(val => {
        return(
            <tr>{val}</tr>
        )
    })

    const secondCol = secondGroup.map(val => {
        return(
            <tr>{val}</tr>
        )
    })

    return(
        <div>
            <table className="first">
                <th>First Group</th>
                {firstCol}
            </table>

            <table className="second">
                <th>Second Group</th>
                {secondCol}
            </table>
        </div>
    )
}
