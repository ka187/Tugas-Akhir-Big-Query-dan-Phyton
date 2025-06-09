SELECT 
    t.tahun,
    t.pendapatan,
    t.beban_operasional,
    t.penyusutan,
    (t.pendapatan - t.beban_operasional - t.penyusutan) AS laba_kena_pajak,
    k.tax_rate,
    CASE 
        WHEN t.tahun BETWEEN k.tax_holiday_awal AND k.tax_holiday_akhir THEN 0
        ELSE k.tax_rate
    END AS tax_rate_applied,
    (t.pendapatan - t.beban_operasional - t.penyusutan) * 
    CASE 
        WHEN t.tahun BETWEEN k.tax_holiday_awal AND k.tax_holiday_akhir THEN 0
        ELSE k.tax_rate
    END AS pajak_dibayar
FROM 
    `perdagangan-cookies-461717.PPH.transaksi_keuangan` t
LEFT JOIN 
    `perdagangan-cookies-461717.PPH.kebijakan_fiskal` k
ON 
    t.tahun = k.tahun
ORDER BY 
    t.tahun;
	SELECT 
    aset_id,
    kategori,
    nilai_perolehan,
    umur_ekonomis,
    metode,
    nilai_perolehan * (2 / umur_ekonomis) AS depresiasi_tahunan
FROM 
    `perdagangan-cookies-461717.PPH.aset_tetap`
WHERE 
    metode = 'saldo_menurun'
ORDER BY 
    aset_id;

SELECT 
    aset_id,
    kategori,
    nilai_perolehan,
    umur_ekonomis,
    metode,
    nilai_perolehan / umur_ekonomis AS depresiasi_tahunan
FROM 
    `perdagangan-cookies-461717.PPH.aset_tetap`
WHERE 
    metode = 'garis_lurus'
ORDER BY 
    aset_id;
	
SELECT 
    tahun,
    SUM(pendapatan) AS pendapatan,
    SUM(beban_operasional) AS beban_operasional,
    SUM(penyusutan) AS penyusutan,
    SUM(pendapatan - beban_operasional - penyusutan) AS laba_rugi_sebelum_pajak
FROM 
    `perdagangan-cookies-461717.PPH.transaksi_keuangan`
GROUP BY 
    tahun
ORDER BY 
    tahun;