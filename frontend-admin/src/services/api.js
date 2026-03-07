import axios from 'axios';

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const getVendas = async () => {
  const response = await api.get('/vendas/');
  const vendas = response.data;
  return vendas.sort((a, b) => new Date(b.data) - new Date(a.data));
};

export const deleteVenda = async (id) => {
  const response = await api.delete(`/vendas/${id}`);
  return response.data;
};

export const updateVenda = async (id, vendaData) => {
  const response = await api.put(`/vendas/${id}`, vendaData);
  return response.data;
};

export default api;
