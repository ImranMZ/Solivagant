import axios from 'axios';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const generateBrand = async (data) => {
  try {
    const response = await api.post('/generate/brand', data);
    return response.data;
  } catch (error) {
    console.error('Error generating brand:', error);
    throw error;
  }
};

export const generateLogo = async (businessName, industry, style = 'minimalist', colorScheme = null) => {
  try {
    const response = await api.post('/generate/logo', null, {
      params: {
        business_name: businessName,
        industry: industry,
        style: style,
        color_scheme: colorScheme,
      },
    });
    return response.data;
  } catch (error) {
    console.error('Error generating logo:', error);
    throw error;
  }
};

export default api;
