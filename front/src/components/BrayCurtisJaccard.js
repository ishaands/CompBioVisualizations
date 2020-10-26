import React from "react"
import { motion, AnimatePresence } from "framer-motion";
import Grid from "@material-ui/core/Grid";
import Typography from "@material-ui/core/Typography";
import "../styles/Hamming.css";
import {useTable} from "react-table";



export default function BrayCurtisJaccard() {
  const site1 = {
    "Species": ['Bears', 'Turkeys', 'Coyotes', 'Deer', 'Groundhogs'],
    "Populations": [5, 7, 0, 2, 8],
	};
	const site2 = {
    "Species": ['Bears', 'Turkeys', 'Coyotes', 'Deer', 'Groundhogs'],
    "Populations": [0, 5, 8, 4, 6],
	};
  const comparisons = ['>', '>', '<', '<', '>'];
  const data = React.useMemo(
    () => [
      {
        species: site1["Species"][0],
        pop: site1["Populations"][0],
        comp: comparisons[0],
        species2: site2["Species"][0],
        pop2: site2["Populations"][0],
      },
      {
        species: site1["Species"][1],
        pop: site1["Populations"][1],
        comp: comparisons[1],
        species2: site2["Species"][1],
        pop2: site2["Populations"][1],
      },
      {
        species: site1["Species"][2],
        pop: site1["Populations"][2],
        comp: comparisons[2],
        species2: site2["Species"][2],
        pop2: site2["Populations"][2],
      },
      {
        species: site1["Species"][3],
        pop: site1["Populations"][3],
        comp: comparisons[3],
        species2: site2["Species"][3],
        pop2: site2["Populations"][3],
      },
      {
        species: site1["Species"][4],
        pop: site1["Populations"][4],
        comp: comparisons[4],
        species2: site2["Species"][4],
        pop2: site2["Populations"][4],
      },
    ],
    []
  )

  const columns = React.useMemo(
    () => [
      {
        Header: 'Habitat I',

        columns: [
          {
            Header: 'Species',
            accessor: 'species',
          },
          {
            Header: 'Population',
            accessor: 'pop',
          }
        ]
      },
      {
        Header: '',
        accessor: 'comp',
      },
      {
        Header: 'Habitat II',

        columns: [
          {
            Header: 'Species',
            accessor: 'species2',
          },
          {
            Header: 'Population',
            accessor: 'pop2',
          }
        ]
      },
    ],
    []
  )

  const  {
    getTableProps,
    getTableBodyProps,
    headerGroups,
    rows,
    prepareRow,
  } = useTable({columns, data})

  return (
		<div className="App"
      style={{
          position: 'absolute', left: '50%', top: '20%',
          transform: 'translate(-50%, -50%)',
      }}
    >
			<Grid container>
        <Grid item xs={12}>
          <div
            style={{
              whiteSpace: "nowrap",
              overflowX: "auto",
            }}
          >
            <Typography style={{ display: "inline" }} variant={"h6"}>
              Habitat I
            </Typography>
          </div>
          <table {...getTableProps()} style={{ border: 'solid 1px blue' }}>
            <thead>
              {headerGroups.map(headerGroup => (
                <tr {...headerGroup.getHeaderGroupProps()}>
                  {headerGroup.headers.map(column => (
                    <th
                      {...column.getHeaderProps()}
                      style={{
                        borderBottom: 'solid 3px red',
                        background: 'aliceblue',
                        color: 'black',
                        fontWeight: 'bold',
                      }}
                    >
                      {column.render('Header')}
                    </th>
                  ))}
                </tr>
              ))}
            </thead>
            <tbody {...getTableBodyProps()}>
              {rows.map(row => {
                prepareRow(row)
                return (
                  <tr {...row.getRowProps()}>
                    {row.cells.map(cell => {
                      return (
                        <td
                          {...cell.getCellProps()}
                          style={{
                            padding: '10px',
                            border: 'solid 1px gray',
                            background: 'papayawhip',
                          }}
                        >
                          {cell.render('Cell')}
                        </td>
                      )
                    })}
                  </tr>
                )
              })}
            </tbody>
          </table>
        </Grid>
			</Grid>
		</div>
	);
}
