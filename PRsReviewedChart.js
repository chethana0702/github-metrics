// PRsReviewedChart.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { PieChart, Pie, Cell, ResponsiveContainer } from 'recharts';

const PRsReviewedChart = () => {
    const [prsReviewedData, setPRsReviewedData] = useState([]);

    useEffect(() => {
        axios.get('http://localhost:5000/prs-reviewed')
            .then(response => setPRsReviewedData(response.data))
            .catch(error => console.error(error));
    }, []);

    // Implement your chart rendering logic here

    const COLORS = ['#0088FE', '#00C49F', '#FFBB28', '#FF8042'];

    return (
        <div>
            <h2>PRs Reviewed Chart</h2>
            <ResponsiveContainer width="100%" height={300}>
                <PieChart>
                    <Pie
                        dataKey="value"
                        isAnimationActive={false}
                        data={prsReviewedData}
                        cx="50%"
                        cy="50%"
                        outerRadius={80}
                        fill="#8884d8"
                        label
                    >
                        {prsReviewedData.map((entry, index) => (
                            <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                        ))}
                    </Pie>
                </PieChart>
            </ResponsiveContainer>
        </div>
    );
};

export default PRsReviewedChart;
