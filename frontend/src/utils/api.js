import axios from 'axios';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: { 'Content-Type': 'application/json' },
});

export const generateBrand = async (data) => {
  const response = await api.post('/generate/brand', data);
  return response.data;
};

export const twistBrand = async (data) => {
  const response = await api.post('/generate/twist', data);
  return response.data;
};

export const downloadBrandKit = async (data) => {
  const response = await api.post('/generate/export', data, {
    responseType: 'blob',
  });
  const url = window.URL.createObjectURL(new Blob([response.data]));
  const link = document.createElement('a');
  link.href = url;
  link.setAttribute('download', `${data.business_name || 'brand'}-kit.zip`);
  document.body.appendChild(link);
  link.click();
  link.remove();
  window.URL.revokeObjectURL(url);
};

export default api;
