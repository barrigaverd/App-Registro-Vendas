import axios from 'axios';

const api = axios.create({
  baseURL: 'http://191.252.179.51:8001',
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

export default api;
