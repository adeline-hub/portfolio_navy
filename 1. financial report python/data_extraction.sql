-- Création de la table pour stocker les données financières
CREATE TABLE financial_data (
    id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    category VARCHAR(255) NOT NULL,
    revenue NUMERIC(15, 2) NOT NULL
);

-- Insertion de données fictives
INSERT INTO financial_data (date, category, revenue) VALUES
('2024-01-01', 'Tech', 120000),
('2024-01-02', 'Retail', 95000),
('2024-01-03', 'Finance', 134000),
('2024-01-04', 'Healthcare', 87000);

-- Extraction des revenus par catégorie
SELECT category, SUM(revenue) AS total_revenue
FROM financial_data
GROUP BY category
ORDER BY total_revenue DESC;
