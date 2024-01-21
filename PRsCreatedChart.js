// PRsCreatedChart.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { PieChart, Pie, Cell, ResponsiveContainer } from 'recharts';

const PRsCreatedChart = () => {
    const [prsData, setPRsData] = useState([]);

    useEffect(() => {
        axios.get('http://localhost:5000/prs-created')
            .then(response => setPRsData(response.data))
            .catch(error => console.error(error));
    }, []);

    // Implement your chart rendering logic here

    const COLORS = ['#0088FE', '#00C49F', '#FFBB28', '#FF8042'];

    return (
        <div>
            <h2>PRs Created Chart</h2>
            <ResponsiveContainer width="100%" height={300}>
                <PieChart>
                    <Pie
                        dataKey="value"
                        isAnimationActive={false}
                        data={prsData}
                        cx="50%"
                        cy="50%"
                        outerRadius={80}
                        fill="#8884d8"
                        label
                    >
                        {prsData.map((entry, index) => (
                            <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                        ))}
                    </Pie>
                </PieChart>
            </ResponsiveContainer>
        </div>
    );
};

export default PRsCreatedChart;
