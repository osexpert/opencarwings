*** Begin Patch
*** Update File: db/models.py
@@
 class EVInfo(models.Model):
@@
     last_updated = models.DateTimeField(null=True, default=None, blank=True)
+    # Timestamp when AC was last started (UTC). Cleared when AC is turned off.
+    ac_last_started = models.DateTimeField(null=True, default=None, blank=True)
@@
 class Car(models.Model):
@@
     tcu_type = models.CharField(max_length=32, default='continental2012', choices=TCU_TYPE)
+    # Auto-off settings for AC: enable and timeout in minutes (0 == Never)
+    ac_auto_off_enabled = models.BooleanField(default=False)
+    ac_auto_off_minutes = models.IntegerField(default=0)
*** End Patch