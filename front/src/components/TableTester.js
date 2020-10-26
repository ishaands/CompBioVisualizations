import React from "react"
import { motion, AnimatePresence } from "framer-motion";
import Grid from "@material-ui/core/Grid";
import Typography from "@material-ui/core/Typography";
import "../styles/Hamming.css";
import TableComponent from "./TableComponent.js";
import {useTable} from "react-table";

export default function TableTester() {
  const site1 = [
    {
      "Species": 'Bears',
      "Population": 5,
    },
    {
      "Species": 'Turkeys',
      "Population": 7,
    },
    {
      "Species": 'Coyotes',
      "Population": 0,
    },
    {
      "Species": 'Deer',
      "Population": 2,
    },
    {
      "Species": 'Groundhogs',
      "Population": 8,
    },
  ]
  const site2 = {
    "Species2": ['Bears', 'Turkeys', 'Coyotes', 'Deer', 'Groundhogs'],
    "Population2": [0, 5, 8, 4, 6],
  };

   const data1 = React.useMemo(
     () =>
       site1.map(speciesGroup => {
         return {species: speciesGroup["Species"], population: speciesGroup["Population"]}
       })


       // {
       //   col1: 'Hello',
       //   col2: 'World',
       // },
       // {
       //   col1: 'react-table',
       //   col2: 'rocks',
       // },
       // {
       //   col1: 'whatever',
       //   col2: 'you want',
       // },
     ,
     []
   )

   //site1 is auto-generated from backend

   const columns1 = React.useMemo(
     () => [
       {
         Header: 'Species',
         accessor: 'species', // accessor is the "key" in the data
       },
       {
         Header: 'Population',
         accessor: 'population',
       },
     ],
     []
   )

   const data2 = React.useMemo(
     () => [
       {
         c1: 'Hello',
       },
     ],
     []
   )

   const columns2 = React.useMemo(
     () => [
       {
         Header: 'Column 1',
         accessor: 'c1', // accessor is the "key" in the data
       }
     ],
     []
   )

   return (
     <div>
       <TableComponent columns={columns1} data={data1}/>
       <TableComponent columns={columns2} data={data2}/>
     </div>
   )
}
