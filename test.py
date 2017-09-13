import cv2
from managers import WindowManager, CaptureManager
class Cameo:
	def __init__(self):
		self._windowManager = WindowManager('Cameo',self.onKeypress)
		self._captureManager = CaptureManager(cv2.VideoCapture(0), self._windowManager, True)
	def run(self):
		"""Run the main loop."""
		self._windowManager.createWindow()
		while self._windowManager.isWindowC:
			self._captureManager.enterFrame()
			frame = self._captureManager.frame()
			
			self._captureManager.exitFrame()
			self._windowManager.processEvents()
	
	def onKeypress (self, keycode):
		if keycode == ord('q'): # space
			self._captureManager.writeImage('screenshot.png')
		elif keycode == 9: # tab
			if not self._captureManager.isWritingVideo():
				self._captureManager.startWritingVideo('screencast.avi')
			else:
				self._captureManager.stopWritingVideo()
		elif keycode == 27: # escape
			self._windowManager.destroyWindow()
			self._captureManager._capture.release()
			cv2.destroyAllWindows()
if __name__=="__main__":
	Cameo().run()
