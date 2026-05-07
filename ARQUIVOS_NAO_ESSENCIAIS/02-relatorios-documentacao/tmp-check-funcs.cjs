const { Client } = require('pg');
const c = new Client({
  host: 'db.dproxlygtabihfhtxdvm.supabase.co',
  user: 'postgres.dproxlygtabihfhtxdvm',
  password: '@AbnerI6p4p0a6',
  database: 'postgres',
  port: 5432,
  ssl: { rejectUnauthorized: false }
});
(async () => {
  try {
    await c.connect();
    const names = ['create_order','update_order_status','adjust_flavor_stock','set_product_availability','set_flavor_availability','save_customer','save_store_settings','restore_demo_data','get_next_order_number','validate_kiosk_code'];
    const res = await c.query(
      `SELECT proname FROM pg_proc WHERE pronamespace = 'public'::regnamespace AND proname = ANY($1) ORDER BY proname`,
      [names]
    );
    console.log('Funcoes no Postgres:', res.rows.map(r => r.proname).join(', '));
    await c.end();
  } catch(e) {
    console.log('ERR:', e.message);
  }
})();
