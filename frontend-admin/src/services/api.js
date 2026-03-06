import axios from 'axios';

const api = axios.create({
  baseURL: 'http://191.252.179.51:8001',
  headers: {
    'Content-Type': 'application/json',
  },
});

export const getVendas = async () => {
  const response = await api.get('/vendas/');
  // A API retorna do mais antigo para o mais novo geralmente, vamos ordenar do mais novo para o mais antigo:
  return response.data.sort((a, b) => new Date(b.data) - new Date(a.data));
};

export const updateVenda = async (id, vendaData) => {
  const response = await api.put(`/vendas/${id}`, vendaData);
  return response.data;
};

export default api;
