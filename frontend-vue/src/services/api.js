import axios from 'axios'

const api = axios.create({
  baseURL: 'http://191.252.179.51:8001',
  headers: {
    'Content-Type': 'application/json',
  },
})

export const getSalesToday = async () => {
  try {
    const today = new Date().toLocaleDateString('en-CA')
    const response = await api.get(`/vendas/?data=${today}`)
    return response.data
  } catch (error) {
    console.error('Error fetching sales:', error)
    throw error
  }
}

export const createSale = async (data) => {
  try {
    const response = await api.post('/vendas/', data)
    return response.data
  } catch (error) {
    console.error('Error creating sale:', error)
    throw error
  }
}

export const deleteSale = async (id) => {
  try {
    const response = await api.delete(`/vendas/${id}`)
    return response.data
  } catch (error) {
    console.error(`Error deleting sale ${id}:`, error)
    throw error
  }
}

export const updateSale = async (id, data) => {
  try {
    const response = await api.put(`/vendas/${id}`, data)
    return response.data
  } catch (error) {
    console.error(`Error updating sale ${id}:`, error)
    throw error
  }
}

export default api
